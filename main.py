from modeling.model_saver import ModelSaver


def main():
    saver = ModelSaver().save()
    if saver:
        print("zaebis")
    else:
        print("blyat")


if __name__ == "__main__":
    main()
