with open('lkt_novideo/test.txt', 'r') as f:
    with open('lkt_novideo/test_new.txt', 'w') as w:
        for line in f:
            a = line[1:-2]
            w.write(line)
            w.write(str(3-int(line[0])) + a + '0\n')