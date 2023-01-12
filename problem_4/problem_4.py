class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group: Group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if not user:
        return False

    members = group.get_users()
    if user in members:
        return True
    else:
        sub_groups = group.get_groups()
        for nested in sub_groups:
            if is_user_in_group(user, nested):
                return True

    return False


def nested_membership(user: str, group: Group):
    result = is_user_in_group(user, group)
    return result == True


def membership(user: str, group: Group):
    result = is_user_in_group(user, group)
    return result == True


def not_a_member(user: str, group: Group):
    result = is_user_in_group(user, group)
    return result == False


def null_case(user: None, group: Group):
    result = is_user_in_group(user, group)
    return result == False


if __name__ == "__main__":
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)

    print(nested_membership(sub_child_user, parent))
    # True
    print(membership(sub_child_user, sub_child))
    # True
    print(not_a_member('Udacity', parent))
    # True
    print(null_case(None, parent))
    # True
