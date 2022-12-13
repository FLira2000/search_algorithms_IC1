from Path import Path


def empty(lst):
    return len(lst) == 0


class Labyrinth:
    root = None
    connections = None

    def __init__(self, root_connections, connections):
        print("reading graph connections...")
        root_letter = root_connections['letter']
        self.root = Path(root_letter)
        state = []

        for letter, position in root_connections['connections']:
            print(f"current root node: {letter}")
            self.root.add_path(position, letter)

        for connection_dict in connections:
            connection_letter = list(connection_dict.keys())[0]
            to_connection_letter, direction = list(connection_dict.values())[0].values()
            root_connections_letters = [path_obj.letter for _, path_obj in self.root.to_iter()]
            print(f"current graph node: {connection_letter}")
            if connection_letter not in root_connections_letters:
                tmp = Path(connection_letter)
                tmp.add_path(direction, to_connection_letter)
                state.append(tmp)
            else:
                for direction, path_obj in self.root.to_iter():
                    if path_obj.letter == connection_letter:
                        path_obj.add_path(direction, to_connection_letter)

        print("done.")

    def dfs_search(self, letter_to_found):
        response = None
        opened_stack = [self.root]
        closed_list = []
        success = False
        print("starting depth first based search ...")

        while success is False and len(opened_stack) > 0:
            candidate_node = opened_stack.pop()
            closed_list.append(candidate_node)
            if candidate_node.letter == letter_to_found:
                print(f"actual labyrinth letter: {candidate_node.letter}")
                success = True
                response = candidate_node
            for side, node in candidate_node.to_iter():
                if node.letter == letter_to_found:
                    success = True
                    response = node
                else:
                    opened_stack.append(node)

        print(f"results of search: {success}")
        return (success, response)

    def backtrack_search(self, letter_to_found):
        print("starting backtracking based search ...")
        response = self._backtrack_search([], letter_to_found)

        print(f"results of search: {True if response else False}")
        if not isinstance(response, tuple):
            return (False, None)
        return response

    def _backtrack_search(self,
                          visited_nodes,
                          letter_to_found,
                          current_node=None
                          ):

        current_node = self.root if current_node is None else current_node
        if current_node not in visited_nodes:
            visited_nodes.append(current_node)
            if current_node.letter == letter_to_found:
                print(f"actual labyrinth letter: {current_node.letter}")
                return (True, current_node)
            else:
                for side, node in current_node.to_iter():
                    xpto = self._backtrack_search(visited_nodes, letter_to_found, node)
                    if xpto:
                        return xpto

    def bfs_search(self, letter_to_found):
        def push(q, el):
            return [el, *q]

        response = None
        fifo_opened = [self.root]
        closed_nodes = []
        success = False

        print("starting breadth first based search ...")
        while success is False and len(fifo_opened) > 0:
            candidate_node = fifo_opened.pop()
            closed_nodes.append(candidate_node)
            if candidate_node.letter == letter_to_found:
                success = True
                response = candidate_node
                print(f"actual labyrinth letter:{candidate_node.letter}")
            for side, node in candidate_node.to_iter():
                if node.letter == letter_to_found:
                    success = True
                    response = node
                else:
                    fifo_opened = push(fifo_opened, node)

        print(f"results of search: {success}")
        return (success, response)
