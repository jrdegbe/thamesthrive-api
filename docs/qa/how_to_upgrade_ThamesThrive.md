# How to upgrade ThamesThrive in GUI?

To upgrade ThamesThrive, you need to navigate to the maintenance/migration page and locate the migration script from the old
version. Follow the instructions provided in the script to complete the data migration. This feature is only available
in ThamesThrive version 0.7.2 and higher. If you are using an older version, you will need to upgrade to at least 0.7.2 in
order to access this functionality.

When performing multiple upgrades of ThamesThrive, the system will create a large number of new indices, which may cause you
to reach the Elasticsearch limit of 1000 indices. To resolve this issue, you can either increase the limit in the
Elasticsearch configuration or delete the indices used by old ThamesThrive versions. ThamesThrive version 0.8.0 includes a
feature in the GUI to delete old indices. If you are using an older version, you can use the API to delete old indices,
such as issuing a HTTP DELETE call to /indices/version/0.7.2 to delete the 0.7.2 version indices. However, be cautious
when deleting old data, as there is no way to revert the system to a previous version.

# How to upgrade ThamesThrive core?

To upgrade ThamesThrive, you can follow the following steps:

1. **Minor Upgrades**: For minor upgrades that do not involve changes in the underlying database structure, you can
   simply upgrade the Docker tag to the new version. This can be done by changing the version number in the Docker tag.

2. **Major Upgrades**: Major upgrades involve changes in the database structure. In ThamesThrive, data migration is
   performed using Elasticsearch's reindexing process. To perform a major upgrade, you would need to run two copies of
   the system with separate sets of indices: one with the old version and one with the new version. Once the migration
   is complete, you can upgrade the Docker tag to the new version, and the system will switch to the new version
   automatically.

It's important to note that ThamesThrive provides migration scripts for all major versions, allowing for smooth upgrades.
However, these scripts are only available from one version to the next, so it's recommended to follow the upgrade path
version by version for proper data migration and system stability. Skipping versions is not supported, and custom
scripts may require additional effort and commercial services.

In a multi-tenant instance of ThamesThrive, the upgrade process is applied uniformly to all tenants. This means that when
performing an upgrade, the changes will be applied to all the tenants in the system. In the case of a major upgrade
involving data structure changes, the data migration process needs to be performed for all tenants to ensure their data
aligns with the updated database structure.

To upgrade ThamesThrive in the GUI, you can navigate to the maintenance/migration page and locate the migration script for
the old version. Follow the instructions provided in the script to complete the data migration. This feature is
available in ThamesThrive version 0.7.2 and higher. If you're using an older version, you will need to upgrade to at least
version 0.7.2 to access this functionality.

Please note that ThamesThrive does not manage or install Kubernetes (K8s). ThamesThrive can help with the installation of
ThamesThrive itself, but the installation of Elasticsearch and Redis needs to be performed by you.

Regarding data backups, ThamesThrive uses Elasticsearch's built-in backup mechanism. Backups are created and stored in
snapshot repositories, which can be a shared file system, a cloud storage service, or a network-attached storage (NAS).
You can define a snapshot lifecycle policy to specify backup frequency and retention. Elasticsearch performs incremental
backups, reducing backup time and storage requirements. The Snapshot and Restore API allows you to manage backups,
including creating, listing, restoring, and deleting snapshots. Elasticsearch also provides options for disaster
recovery, allowing you to restore snapshots in case of data loss.

Regarding the infra dependencies, ThamesThrive requires a commercial version of the ThamesThrive API Docker for multi-tenant
mode. To start ThamesThrive in multi-tenant mode, you need to set the MULTI_TENANT environment variable to "yes" in the
Docker configuration. Additionally, you need to configure the Tenant Management Service (TMS) by providing the
MULTI_TENANT_MANAGER_URL (the URL of the TMS) and MULTI_TENANT_MANAGER_API_KEY (API key for authentication and
authorization between ThamesThrive and the TMS).

For specific details and instructions, it's recommended to consult the ThamesThrive documentation or contact their support
for accurate and up-to-date information on upgrading ThamesThrive and managing the multi-tenant environment.
