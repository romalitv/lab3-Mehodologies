from fastapi import APIRouter
import numpy

router = APIRouter()

@router.get('/matrix')
def matrix() -> dict:
    
    matrix_1 = numpy.random.rand(10, 10)
    matrix_2 = numpy.random.rand(10, 10)
    product = numpy.dot(matrix_1, matrix_2)

    res = {
        "matrix_a": matrix_1.tolist(),
        "matrix_b": matrix_2.tolist(),
        "product": product.tolist()
    }

    return res