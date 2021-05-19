class Accounts(object):
    def __init__(self, client):
        self.client = client

    def create_a_account(self, data):
        """
        Create a new account


        Args:
            data:

        Returns:

        """
        return self.client._post("/accounts", json=data)

    def retrieve_a_account(self, account_id):
        """
        Retrieve an existing contact


        Args:
            account_id:

        Returns:

        """
        return self.client._get("/accounts/{}".format(account_id))

    def update_a_account(self, account_id, data):
        """
        Update an existing account


        Args:
            account_id:
            data:

        Returns:

        """
        return self.client._put("/accounts/{}".format(account_id), json=data)

    def delete_a_account(self, account_id):
        """
        Delete an existing contact


        Args:
            account_id:

        Returns:

        """
        return self.client._delete("/accounts/{}".format(account_id))

    def list_all_accounts(self, **params):
        """
        Returns:

        """
        return self.client._get("/accounts", params=params)


    def associate_contact(self, data):
        """
        Returns:

        """
        return self.client._post("/accountContacts", json=data)

    def associate_contacts(self):
        """
        Returns:
        """
        return self.client._get(f"/accountContacts/")

    def associate_update_contact(self, account_id):
        raise NotImplementedError

    def associate_delete_contact(self, account_id):
        raise NotImplementedError

