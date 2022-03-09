if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='testing')
    parser.add_argument('--bar', type=str, help='an int boolean flag')
    parser.add_argument('--barry', type=str, help='an int boolean flag')
    #parser.add_argument('--config', type=str, help='an int boolean flag')
    #parser.add_argument('--strategy', type=str, help='an int boolean flag')

    args = parser.parse_args()
    print(args)
    print(f'You provided bar={args.bar}, barry={args.barry}')
