from typing import Optional

from fastapi import APIRouter, HTTPException

from tracardi.domain.payload.customer_consent import CustomerConsent
from tracardi.domain.profile import Profile, ConsentRevoke
from tracardi.service.storage.driver import storage

router = APIRouter()


@router.post("/customer/consent", tags=["customer"])
async def add_consent_type(data: CustomerConsent, all: Optional[bool] = False):
    """
    Adds customer consent
    """
    session = await storage.driver.session.load_by_id(data.session.id)
    profile = await storage.driver.profile.load_by_id(data.profile.id)
    source = await storage.driver.event_source.load(data.source.id)

    if not source or not profile or not session:
        raise HTTPException(status_code=403, detail="Access denied")

    profile = profile.to_entity(Profile)
    if all:
        for consent in await storage.driver.consent_type.load_all():
            profile.consents[consent['id']] = ConsentRevoke()

    else:
        for consent, flag in data.consents.items():
            if flag:
                profile.consents[consent] = ConsentRevoke()
            else:
                if consent in profile.consents:
                    del profile.consents[consent]
    profile.aux['consents'] = {"displayed": True}
    return await storage.driver.profile.save(profile)
