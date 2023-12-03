from hero import get_hero, hero_id_list


def main():
    for hero_id in hero_id_list():
        print(hero_id)
        hero = get_hero(hero_id)
        print(hero.data["Model"])


if __name__ == "__main__":
    main()
