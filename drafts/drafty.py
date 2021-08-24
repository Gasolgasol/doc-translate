from hurry.filesize import size, si

stringy = "5eff6143-59cf-434a-ba67-11e36307b567.pdf"
print(stringy[:-4])

print(size(145687, system=si))