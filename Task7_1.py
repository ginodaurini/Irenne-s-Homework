class Matrix:
    def __init__(self, z_1, z_2):
        # self.array = [z_1, z_2]
        self.z_1 = z_1
        self.z_2 = z_2

    def __add__(self):
        array = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]

        for i in range(len(self.z_1)):

            for j in range(len(self.z_2[i])):
                array[i][j] = self.z_1[i][j] + self.z_2[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in array]))


    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in array]))



my_matrix = Matrix([[7, 13, 21],
                    [9, 18, 33],
                    [43, 55, 11]],
                   [[22, 15, 1],
                    [59, 69, 101],
                    [5, 83, 69]])
# result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


print(my_matrix.__add__())
