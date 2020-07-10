def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    needed_weights = {}

    for current_index in range(len(weights)):
        current_weight = weights[current_index]

        #if key is found, then other weight was inserted previously
        if current_weight in needed_weights:

            #get index of other weight
            previous_index = needed_weights[current_weight]

            #return tuple with current weight index
            return (current_index, previous_index)
        
        #store info about current weight with
        # key:other weight needed value:current index
        needed_weights[limit-current_weight] = current_index

    return None
