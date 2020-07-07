import record
import train
import test

print("Enter your choice \n[1] New User \n[2] Existing User\n")
ch = input()

if ch=="1":
    record.face_record()
    train.train_model()
    mar = input("\nWant to mark your attendence ? (y/n)\n")
    if mar=="y" or mar=="Y":
        test.test_model()
    else:
        exit()

elif ch=="2":
    test.test_model()
