import logging

## Logging setting
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]
)

logger=logging.getLogger("ArithematicApp")

def add(a,b):
    result=a+b
    logging.debug(f"Adding {a}+{b}={result}")
    return result

def subtract(a,b):
    result=a-b
    logging.debug(f"Subtracting {a}-{b}={result}")
    return result

def multiply(a,b):
    result=a*b
    logger.debug(f"Multiplying {a}*{b}={result}")
    return result

def divide(a,b):
    try:
        result=a/b
        logger.debug(f"Dividing {a}/{b}={result}")
        return result
    except ZeroDivisionError:
        logging.error("Division by zero error")
        return None
    
add(10,15)
subtract(15,10)
multiply(10,20)
divide(20,10)