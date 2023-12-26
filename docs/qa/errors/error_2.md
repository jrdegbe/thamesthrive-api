# How can the "Address already in use" issue in ThamesThrive be resolved?

To resolve the "Address already in use" issue in ThamesThrive, you can remap the port that ThamesThrive is running on. By
changing the port mapping in the Docker run command, you can assign a different port for ThamesThrive to use, such as
changing from 8686 to 8888. Additionally, if you are using ThamesThrive's GUI, you will also need to update the API URL to
reflect the new port.
