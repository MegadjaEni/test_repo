import bcrypt

class User:
    def __init__(self, username, password):
        self.username = username
        self.password_hash = self.__hash_password(password)

    def __hash_password(self, password):
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode('utf-8'), salt)

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash)

    def __str__(self):
        return f"Felhasználó: {self.username}"


class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, username, password):
        if any(user.username == username for user in self.users):
            raise ValueError(f"A {username} nevű felhasználó már létezik")
        new_user = User(username, password)
        self.users.append(new_user)
        print(f"Felhasználó hozzáadva: {username}")

    def authenticate(self, username, password):
        for user in self.users:
            if user.username == username:
                if user.check_password(password):
                    print("Sikeres hitelesítés")
                    return True
                else:
                    print("Helytelen jelszó")
                    return False
        print("A felhasználó nem található")
        return False

    def list_users(self):
        if not self.users:
            print("Nincs regisztrált felhasználó")
        else:
            print("Felhasználók listája:")
            for user in self.users:
                print(user)


user_manager = UserManager()

user_manager.add_user("Elek", "valami")
user_manager.add_user("Jakab", "jelszoo")

user_manager.list_users()


