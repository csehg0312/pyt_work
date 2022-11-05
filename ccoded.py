from instant import inline
    sieve_code = """
    PyObject* prime_list(int max) {
        PyObject *list = PyList_New(0);
        int *numbers, *end, *n; 
        numbers = (int *) calloc(sizeof(int), max);
        end = numbers + max;

        numbers[2] = 2;
        for (int i = 3; i < max; i += 2) { numbers[i] = i; }
        for (int i = 3; i < sqrt(max); i++) {
            if (numbers[i] != 0) {
                for (int j = i + i; j < max; j += i) { numbers[j] = 0; }
            }
        }
        for (n = numbers; n < end; n++) { 
            if (*n != 0) { PyList_Append(list, PyInt_FromLong(*n)); }
        }
        free(numbers);
        return list;
    }
    """
    sieve = inline(sieve_code)