import argparse

if __name__ == '__main__':

  parser.add_argument("-a", "--a",type=str, required=True)
  parser.add_argument("-b", "--b",type=str, required=True)

  args = parser.parse_args()

  a=args.a
  b=args.b

  soma=a+b

  print(soma)
