from nbody import combinations, SOLAR_MASS, DAYS_PER_YEAR, BODIES, SYSTEM, PAIRS, NAMES, \
    advance, report_energy, offset_momentum
import time

# added to GIT
def input_control_flag():
    print("the output content is as follows: ")
    print("0(default): output name and position of each body")
    print("1: output name, position and velocity of each body")
    print("2: output name, position, velocity and mass of each body")
    print("3: DO NOT output")
    input_number = input("please enter the index of the output content: ")
    mode = int(input_number)
    return mode

def input_control_iteration():
    print("How many times do you want to iterate? ")
    input_number = input("please enter the integer value of the iteration time: ")
    iterate_time = int(input_number)
    return iterate_time


if __name__ == "__main__":
    mode = input_control_flag()
    i_times=input_control_iteration()
    start_time=time.time()
    with open('test.csv', 'w') as fh:
        if mode == 0:
            fh.writelines('{}{}'.format('BodyName;X;Y;Z','\n'))
            for times in range(i_times):
                main()
                for i in range(5):
                    fh.writelines(
                        '{},{},{},{}{}'.format(str(NAMES[i]), str(SYSTEM[i][0][0]), str(SYSTEM[i][0][1]),
                                               str(SYSTEM[i][0][2]),
                                               '\n'))
        elif mode == 1:
            fh.writelines('{}{}'.format('BodyName;X;Y;Z;Vx;Vy;Vz','\n'))
            for times in range(i_times):
                main()
                for i in range(5):
                    fh.writelines(
                        '{},{},{},{},{},{},{}{}'.format(str(NAMES[i]), str(SYSTEM[i][0][0]), str(SYSTEM[i][0][1]),
                                                         str(SYSTEM[i][0][2]), str(SYSTEM[i][1][0]),
                                                         str(SYSTEM[i][1][1]), str(SYSTEM[i][1][2]), '\n'))
        elif mode == 2:
            fh.writelines('{}{}'.format('BodyName;X;Y;Z;Vx;Vy;Vz,Mass','\n'))
            for times in range(i_times):
                main()
                for i in range(5):
                    fh.writelines(
                        '{},{},{},{},{},{},{},{}{}'.format(str(names[i]), str(SYSTEM[i][0][0]), str(SYSTEM[i][0][1]),
                                                            str(SYSTEM[i][0][2]), str(SYSTEM[i][1][0]),
                                                            str(SYSTEM[i][1][1]), str(SYSTEM[i][1][2]),
                                                            str(SYSTEM[1][2]), '\n'))
        elif mode == 3:
            print("No output generated.")

        end_time = time.time()
        run_time=end_time-start_time
        print('{} {} {} {}'.format(i_times,'times iterations take', run_time, 'second in total'))






