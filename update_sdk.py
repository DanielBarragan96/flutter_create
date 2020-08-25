with open("android/app/build.gradle", "r+") as f:
     new_file = f.read() # read everything in the file
     f.seek(0) # rewind
     new_file = new_file.replace("compileSdkVersion 28", "compileSdkVersion 29")
     new_file = new_file.replace("minSdkVersion 16", "minSdkVersion 24")
     new_file = new_file.replace("targetSdkVersion 28", "targetSdkVersion 29")
     f.write(new_file) # write the new line before
