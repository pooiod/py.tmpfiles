import requests

class TmpFiles:
    """
    A Python client for the tmpfiles.pooiod7.workers.dev API.
    """
    def __init__(self, base_url="https://tmpfiles.pooiod7.workers.dev/"):
        """
        Initializes the TmpFiles client.

        Args:
            base_url: The base URL of the tmpfiles API.
        """
        self.base_url = base_url

    def set_file(self, filename: str, content: str, time: int = 60) -> requests.Response:
        """
        Creates or updates a file with the given content.

        Args:
            filename: The name of the file to store.
            content: The data to store.
            time: The duration in minutes for which the file will be stored. Defaults to 60.

        Returns:
            The response from the API.
        """
        params = {"filename": filename, "time": time}
        return requests.post(f"{self.base_url}set", params=params, data=content)

    def get_file(self, filename: str) -> requests.Response:
        """
        Retrieves the content of a file.

        Args:
            filename: The name of the file to retrieve.

        Returns:
            The response from the API.
        """
        params = {"filename": filename}
        return requests.get(f"{self.base_url}get", params=params)

    def renew_file(self, filename: str, time: int) -> requests.Response:
        """
        Extends the lifetime of an existing file.

        Args:
            filename: The name of the file to renew.
            time: The additional duration in minutes to store the file.

        Returns:
            The response from the API.
        """
        params = {"filename": filename, "time": time}
        return requests.post(f"{self.base_url}renew", params=params)

    def remove_file(self, filename: str) -> requests.Response:
        """
        Deletes a file.

        Args:
            filename: The name of the file to remove.

        Returns:
            The response from the API.
        """
        params = {"filename": filename}
        return requests.post(f"{self.base_url}remove", params=params)
