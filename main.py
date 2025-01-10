import numpy as np

def solving_func(A,B):
    
    if type(A) != np.ndarray:
        raise ValueError("Macierz A jest w nieodpowiednim formacie")
    elif type(B) != np.ndarray:
        raise ValueError("Macierz B jest w nieodpowiednim formacie")
    elif A.shape[0] != A.shape[1]:
        raise np.linalg.LinAlgError("Macierz A nie jest kwadratowa")
        
    elif A.ndim != 2:
        raise ValueError("Macierz A musi być dwu wymiarowa")
    elif B.ndim != 1:
        raise ValueError("Macierz B musi być jedno wymiarowa")
    elif np.linalg.det(A) == 0:
        raise ValueError("Macierz A jest osobliwa")
    else:
        return np.dot(np.linalg.inv(A),B)
    


   
if __name__=='__main__':
     A = np.array([[1, 7, 3, 5], 
                  [8, 4, 6, 2], 
                  [2, 6, 4, 8], 
                  [5, 3, 7, 1]])
     B = np.array([16, -16, 16, -16])

     x = solving_func(A, B)
    