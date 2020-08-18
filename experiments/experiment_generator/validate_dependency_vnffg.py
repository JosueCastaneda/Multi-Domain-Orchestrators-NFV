import pickle


def check_entries_are_different(entries):
    m1_first = entries[0]['first_connection_point']
    m2_first = entries[1]['first_connection_point']
    m3_first = entries[2]['first_connection_point']
    m4_first = entries[3]['first_connection_point']
    m1_second = entries[0]['second_connection_point']
    m2_second = entries[1]['second_connection_point']
    m3_second = entries[2]['second_connection_point']
    m4_second = entries[3]['second_connection_point']
    if m1_first == m2_first and m2_first == m3_first and m3_first == m4_first:
        pass
    else:
        print('M1: ', m1_first, ' M2: ', m2_first, ' M3: ', m3_first, ' M4: ', m4_first)
        return True
    if m1_second == m2_second and m2_second == m3_second and m3_second == m4_second:
        pass
    else:
        print('M1: ', m1_second, ' M2: ', m2_second, ' M3: ', m3_second, ' M4: ', m4_second)
        return True
    return False


def main():
    m1 = pickle.load(open('vnf_fg_infoorch_1.p', 'rb'))
    m2 = pickle.load(open('vnf_fg_infoorch_2.p', 'rb'))
    m3 = pickle.load(open('vnf_fg_infoorch_3.p', 'rb'))
    m4 = pickle.load(open('vnf_fg_infoorch_4.p', 'rb'))

    inconsistencies = 0

    for i in range(0, len(m1)):
        for j in range(0, len(m1[0])):
            m1_service = m1[i][j]
            m2_service = m2[i][j]
            m3_service = m3[i][j]
            m4_service = m4[i][j]
            entries = [m1_service, m2_service, m3_service, m4_service]
            if check_entries_are_different(entries):
                inconsistencies += 1
    print('Inconsistencies: ', inconsistencies)


if __name__ == '__main__':
    main()
