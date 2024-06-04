from pprint import pprint
import tools


def main():
    try:
        all_data:dict[any]=tools.GetDownload_Json()
    except Exception as error:
        print(error)
    else:
        data:list[dict]=tools.get_date(all_data)
        pprint(data)

if __name__ =="__main__":
    main()