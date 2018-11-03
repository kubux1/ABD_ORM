import logging
import role as rl

logging.basicConfig(level=logging.DEBUG)

LOG = logging.getLogger("root")


class Rbac:
    def __init__(self):
        """
        Initializes RBAC system.
        """
        self.roles = {}
        self.users = {}

    def get_user_roles(self, user):
        """
        Returns roles assigned to user.
        :param user:
        :return: list of role dicts
        """
        LOG.info("[RBAC] Query: Roles of user {} are: {}".format(
            user, self.users[user]['roles']
        ))
        return self.users[user]['roles']

    def add_role(self, role):
        self.roles[role.name] = role
        LOG.info("[RBAC] Role {} added to RBAC.".format(role.name))

    def assign_role_to_user(self, user, role_name):
        """
        Assigns a role to a user.
        :param user:
        :param role_name:
        :return:
        """
        self.users[user]['roles'][role_name] = self.roles[role_name]
        LOG.info("[RBAC] Role {} assigned to user {}.".format(role_name, user))

    def multi_assign_role_to_user(self, user, roles_names):
        """
        Assigns many roles to a user.
        :param user:
        :param roles_names: list of role names
        :return:
        """
        for role_name in roles_names:
            self.users[user]['roles'][role_name] = self.roles[role_name]
            LOG.info("[RBAC] Role {} assigned to user {}.".format(role_name, user))

    def add_user(self, user, password):
        """
        Add a user as an immutable tuple(login, password).
        :param user:
        :param password:
        :return:
        """
        self.users[user] = {
            'password': password,
            'roles': {}
        }
        LOG.info("[RBAC] User {} added to RBAC system.".format(user))


rbac = Rbac()

# Zdefiniowanie ról
roles = ["coachCreator", "coachEditor", "coachSelector", "coachDeleter",
         "gymCreator", "gymEditor", "gymSelector", "gymDeleter",
         "clientCreator", "clientEditor", "clientSelector", "clientDeleter",
         "termCreator", "termEditor", "termSelector", "termDeleter",
         "groupClassCreator", "groupClassEditor", "groupClassSelector",
         "groupClassDeleter", "enrollmentCreator", "enrollmentEditor",
         "enrollmentSelector", "enrollmentDeleter"
         ]

# Dodanie ról do systemu
for name in roles:
    rbac.add_role(rl.Role(name))

# Dodanie przykłądowych uzytkowników systemu
rbac.add_user('hr_user1', '1234')
rbac.multi_assign_role_to_user('hr_user1', ['coachSelector', 'coachDeleter',
                                            'coachCreator', 'coachEditor'])
rbac.add_user('gym_owner1', '1234')
rbac.multi_assign_role_to_user('gym_owner1', ['coachSelector', 'gymEditor',
                                              'gymSelector'])
rbac.add_user('receptionist1', '1234')
rbac.multi_assign_role_to_user('receptionist1', ['clientEditor',
                                                 'clientSelector',
                                                 'termSelector',
                                                 'enrollmentSelector'])

# Sprawdzenie hasła
# proba_hasla = '1234'
# if rbac.users['hr_user1']['password'] == proba_hasla:
#     print("wpisane haslo jest ok")
# else:
#     print("wpisane haslo jest złe")

# Definicja i dodanie roli
# rola = rl.Role('coachEditor')
# rola2 = rl.Role('coachSelector')
#
# rbac.add_role(rola)
# rbac.add_role(rola2)
#
# Kontrola dostępu dla uzytkownika user1
# if 'edytor_coachow' in rbac.get_user_roles('hr_user1'):
#     print("przyciski dla hr_user1 to: {}".format(
#         rbac.get_user_roles('hr_user1')['edytor_coachow'].get_accesses()
#     ))
#     # dodaj do gui przycisk dodawania i usuwania coachów
#     pass
#
# if 'przegladacz_coachow' in rbac.get_user_roles('hr_user1'):
#     print("przyciski dla hr_user1 to: {}".format(
#         rbac.get_user_roles('hr_user1')['przegladacz_coachow'].get_accesses()
#     ))
#     # dodaj do gui przycisk wyszukiwania(select) coachów
#     pass