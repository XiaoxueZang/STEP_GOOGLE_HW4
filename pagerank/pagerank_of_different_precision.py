import sys


# class SeachFamous:
# self.relation_graph is the dictionary to store the relation between nodes
# in the format like {'start node': ['end node1', 'end node2']}
# [start node, end node1] and [start node, end node2] are edges

# self.person_score is to record the score of each node
# self.person_next_score indicates the next score of each node after one round of calculation

class SearchFamous:
    def __init__(self, filename, initial_score):
        self.relation_graph = {}
        self.person_score = {}
        self.people_number = 0
        self.total_scores = 0
        self.initial_score = initial_score
        self.person_score_next = {}
        self.initiate_graph(filename)

    # initiate_graph is to initialize all the necessaey values based on the information in the file
    def initiate_graph(self, filename):
        file = open(filename, 'r')
        self.people_number = int(file.readline().rstrip())
        self.total_scores = (self.people_number) * (self.initial_score)
        edge_part = False
        for line in file.readlines():
            line = line.rstrip()
            if str.isnumeric(line):
                edge_part = True
                continue
            if edge_part is False:
                self.person_score[line] = self.initial_score
                self.person_score_next[line] = 0
            elif edge_part:
                edge = line.split(' ')
                start_node = edge[0]
                end_node = edge[1]
                if start_node not in self.relation_graph.keys():
                    self.relation_graph[start_node] = [end_node]
                elif start_node in self.relation_graph.keys():
                    self.relation_graph[start_node].append(end_node)

    # this function is to calculate the score of each nodes for XX rounds
    def calculate_rank(self, rounds):
        print("start calculation of the score of each person")
        for i in range(rounds):
            for person in self.person_score.keys():
                scores_flow_out = float(self.person_score[person]) / len(self.relation_graph[person])
                # I do not know whether I should use round() function to determine
                # the next output value from each node, like
                # scores_flow_out = round((self.person_score[person])/len(self.relation_graph[person]))
                for x in self.relation_graph[person]:
                    self.person_score_next[x] += scores_flow_out
            # this is to call the function to check whether the calculation is correct and whether has converged
            continue_calculation = self.refresh_scores()
            if continue_calculation is False:
                print("the balance has been reached in round {0}".format(i))
                self.print_scores()
                return
        self.print_scores()

    # this function is to refresh the score of each node and check whether the score has converged
    def refresh_scores(self) -> object:
        count_same = 0
        total_scores = 0
        for person in self.person_score.keys():
            next_score = self.person_score_next[person]
            total_scores += next_score
            if abs(self.person_score[person] - next_score) <= 0.00001:
                # I need to decide the definition of convergence here, (the precision of calculation)
                count_same += 1
            self.person_score[person] = next_score
            self.person_score_next[person] = 0

        # for debugging
        if int(total_scores - self.total_scores):
            print("the calculation is wrong. "
                  "the false total scores is {0}."
                  "the true total scores is {1}".format(total_scores, self.total_scores))
        # sys.exit(1)
        # return False
        if count_same == self.people_number:
            return False
        return True

    # this is the function to display the final scores of each node
    def print_scores(self):
        for (person, scores) in self.person_score.items():
            print("{0} has score {1}".format(person, scores))


new = SearchFamous("large_data.txt", 100)
new.calculate_rank(1000)
