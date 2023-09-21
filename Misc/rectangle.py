from FinalReview import Rectangle

def main():

    rec1_height = int(input('Enter the height of rectangle 1'))
    rec1_width = int(input('Enter the width for rectangle 1'))
    rec1_area = rec1_height * rec1_width
    rec1_perimeter = (rec1_height * 2) + (rec1_width * 2)


    rec2_height = int(input('Enter the height of rectangle 2'))
    rec2_width = int(input('Enter the width for rectangle 2'))
    rec2_area = rec2_height * rec2_width
    rec2_perimeter = (rec2_height * 2) + (rec2_width * 2)

    rectangle1 = Rectangle(rec1_height, rec1_width)
    rectangle2 = Rectangle(rec2_height, rec2_width)


    if rec1_height > rec2_height:
        return print(f'The height for rectangle 1 is: {rec1_height}, and the width is {rec1_width}, the area is {rec1_area}, finally the perimeter is {rec1_perimeter}.')
    elif rec2_height > rec1_height:
        return print(f'The height for rectangle 2 is: {rec2_height}, and the width is {rec2_width}, the area is {rec2_area}, finally the perimeter is {rec2_perimeter}.')
    

main()

