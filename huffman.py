import heapq

def huffman_encode(symbols, probabilities):
  """Encodes a list of symbols using Huffman coding.

  Args:
    symbols: A list of symbols to be encoded.
    probabilities: A list of probabilities for each symbol.

  Returns:
    A dictionary mapping symbols to their Huffman codes.
  """

  # Create a priority queue of nodes, where each node represents a symbol and has
  # a priority equal to the symbol's probability.
  queue = [(prob, symbol) for prob, symbol in zip(probabilities, symbols)]

  # While the priority queue has more than one node, merge the two nodes with
  # the highest priorities.
  while len(queue) > 1:
    prob1, symbol1 = heapq.heappop(queue)
    prob2, symbol2 = heapq.heappop(queue)

    # Create a new node with a probability equal to the sum of the two
    # merged nodes' probabilities.
    prob = prob1 + prob2
    node = (prob, symbol1 + symbol2)

    # Add the new node to the priority queue.
    heapq.heappush(queue, node)

  # The last node in the priority queue is the root of the Huffman tree.
  huffman_tree = queue[0][1]

  # Create a dictionary mapping symbols to their Huffman codes.
  huffman_codes = {}
  def traverse(node, code):
    if isinstance(node, str):
      huffman_codes[node] = code
    else:
      traverse(node[0], code + '0')
      traverse(node[1], code + '1')

  traverse(huffman_tree, '')

  return huffman_codes

def average_code_length(symbols, probabilities, huffman_codes):
  """Calculates the average length of the Huffman codes for a list of symbols.

  Args:
    symbols: A list of symbols to be encoded.
    probabilities: A list of probabilities for each symbol.
    huffman_codes: A dictionary mapping symbols to their Huffman codes.

  Returns:
    The average length of the Huffman codes.
  """

  total_length = 0
  for symbol, probability in zip(symbols, probabilities):
    code = huffman_codes[symbol]
    total_length += len(code) * probability

  return total_length / sum(probabilities)

def percentage_saved(original_length, compressed_length):
  """Calculates the percentage of space saved by using Huffman encoding.

  Args:
    original_length: The length of the original data.
    compressed_length: The length of the compressed data.

  Returns:
    The percentage of space saved by using Huffman encoding.
  """

  return 100 * (original_length - compressed_length) / original_length

# Example usage:

symbols = ('a2', 'a6', 'al', 'a4', 'a3', 'a5')
probabilities = (0.4, 0.3, 0.1, 0.1, 0.06, 0.04)

# Encode the symbols using Huffman coding.
huffman_codes = huffman_encode(symbols, probabilities)

# Calculate the average code length.
average_code_length = average_code_length(symbols, probabilities, huffman_codes)

# Calculate the percentage of space saved by using Huffman encoding.
original_length = len(symbols) * 5
compressed_length = average_code_length * len(symbols)
percentage_saved = percentage_saved(original_length, compressed_length)

# Print the results.
print(f'Average code length: {average_code_length:.2f} bits/symbol')
print(f'Percentage saved: {percentage_saved:.2f}%')
