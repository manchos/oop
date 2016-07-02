# -*- coding: utf-8 -*-

class Friends:
    """
    Returns a new Friends instance.
    "connections" is an iterable of sets with two elements in each.
    Each connection contains two names as strings.
    Connections can be repeated in the initial data, but inside it's stored once.
    Each connection has only two states - existing or not.
    """
    connections = []
    def __init__(self, connections):
        self.connections = []
        for i in connections:
            if i not in self.connections:
                self.connections.append(i)

    def add(self, connection):
        """
        Add a connection in the instance.
        "connection" is a set of two names (strings).
        Returns True if this connection is new.
        Returns False if this connection exists already.
        """
        if connection in self.connections:
                return False
        self.connections.append(connection)
        return True

    def remove(self, connection):
        """
        Remove a connection from the instance. "connection" is a set of two names (strings).
        Returns True if this connection exists.
        Returns False if this connection is not in the instance.
        """
        if connection in self.connections:
                self.connections.remove(connection)
                return True
        return False

    def names(self):
        """
        Returns a set of names. The set contains only names which are connected with somebody.
        """
        nset = set()
        for i in self.connections:
            nset.add(i.pop())
            nset.add(i.pop())
        return nset

    def connected(self, name):
        """
        Returns a set of names which is connected with the given "name".
        If "name" does not exist in the instance, then return an empty set.
        """
        conset = set()
        for i in self.connections:
            if name in i:
                i.remove(name)
                conset.add(i.pop())
        return conset


# функция алгоритма последствий выполнения кода
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
    digit_friends = Friends([{"1", "2"}, {"3", "1"}])
    assert letter_friends.add({"c", "d"}) is True, "Add"
    assert letter_friends.add({"c", "d"}) is False, "Add again"
    assert letter_friends.remove({"c", "d"}) is True, "Remove"
    assert digit_friends.remove({"c", "d"}) is False, "Remove non exists"
    assert letter_friends.names() == {"a", "b", "c"}, "Names"
    assert letter_friends.connected("d") == set(), "Non connected name"
    assert letter_friends.connected("a") == {"b", "c"}, "Connected name"