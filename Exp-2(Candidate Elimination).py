data = [
    ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Sunny', 'Warm', 'High',   'Strong', 'Warm', 'Same', 'Yes'],
    ['Rainy', 'Cold', 'High',   'Strong', 'Warm', 'Change', 'No'],
    ['Sunny', 'Warm', 'High',   'Strong', 'Cool', 'Change', 'Yes']
]
S = ['0', '0', '0', '0', '0', '0']
G = ['?', '?', '?', '?', '?', '?']
print("S0 =", S)
print("G0 =", G)
for n, example in enumerate(data, start=1):
    attributes = example[:-1]
    target = example[-1]
    if target == 'Yes':
        for i in range(len(S)):
            if S[i] == '0':
                S[i] = attributes[i]
            elif S[i] != attributes[i]:
                S[i] = '?'
        print("\nExample", n, "(Positive)")
        print("S" + str(n) + " =", S)
        print("G" + str(n) + " =", G)

    else:
        for i in range(len(G)):
            if G[i] == '?':
                if S[i] != attributes[i]:
                    G[i] = S[i]
        print("\nExample", n, "(Negative)")
        print("S" + str(n) + " =", S)
        print("G" + str(n) + " =", G)
