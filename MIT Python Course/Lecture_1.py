# Lecture 2
"""
variables are objects of type
    int
    float
    char
    string
    BOOLEAN

    assignements are done by =
    true false ==
    stored in memory as variable name
    // div floor
    % remainder
    ** exponent
"""
def print_radius(array):
    for i in array:
        print(i)
    return


def main():
    array=[[1,2,3],[4,5],[6,7,8]]
    for row in range(len(array)):
        for col in range(len(array[row])):
            array[row][col] = col*2+4**row
    print_radius(array)

main()
