from PIL import Image
from image_converter import ListToImage, ImageToList

def main():
  # Open the image.
  dog_img = Image.open("joon.png")
  pixels = ImageToList(dog_img)

  # Apply the custom filter.
  filtered_pixels = apply_filter(pixels)
  print(pixels[8][3])
  print(pixels[2][4])
  # Save an image
  filtered_image = ListToImage(filtered_pixels)
  filtered_image.save("dog_filtered.png")
  return

def apply_filter(pixels):
  # The variable new_pixels will contains the grayscale image.
  new_pixels = []

  for row in range(len(pixels)):
      new_row = []
      for col in range(len(pixels[row])):
        if col+1<len(pixels[row]) and row+1<len(pixels):
          B=3
          C=7
          D=9
        

          r, g, b = pixels[row][col]
          rn,gn,bn = pixels[row][col+1]


          if (r-rn<=B and rn-r<=B) and(gn-g<=B and gn-g<=B) and (bn-b<=B and bn-b<=B):
            new_row.append((200,200,200))
          elif(rn-r<=C and rn-r<=C) and(gn-g<=C and gn-g<=C) and (bn-b<=C and bn-b<=C):
            new_row.append((160,160,160))
          elif (rn-r<=D and rn-r<=D) and(gn-g<=D and gn-g<=D) and (bn-b<=D and bn-b<=D):
            new_row.append((100,100,100))
          else:
            new_row.append((40,40,40))
        else:
          new_row.append((0,0,0))

      new_pixels.append(new_row)
      
  return new_pixels


main()
