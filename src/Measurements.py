import time
import tracemalloc

def measure_algorithm(algorithm, graph):
    #Medição de tempo e espaço de memória
    start_time = time.time()
    tracemalloc.start()
    
    result = algorithm(graph)
    
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    execution_time = time.time() - start_time
    
    return execution_time, result, current, peak
