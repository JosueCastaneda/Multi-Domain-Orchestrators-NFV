import pickle


def check_entries_are_different(entries):
    m1_first = entries[0]['first_connection_point']
    m1_second = entries[0]['second_connection_point']
    for i in range(1, len(entries)):
        m_entry_first = entries[i]['first_connection_point']
        m_entry_second = entries[i]['first_connection_point']
        if m1_first != m_entry_first or m1_second != m_entry_second:
            return True
        m1_first = m_entry_first
        m1_second = m_entry_second

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