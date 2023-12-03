import os
from hero import get_hero, hero_id_list
from util import float_eye
import template


def render_hero(hero_id) -> str:
    hero = get_hero(hero_id)
    print('Rendering hero: ' + hero.display_name)

    """
    def make_level_data(level: int):
        health = float(hero.data['StatusHealth'])
        health += float(hero.data['AttributeBaseStrength']) + float(hero.data['AttributeStrengthGain']) * (level - 1)
        return {
            'level': level,
            'health': hero.data['AttributeBaseStrength'] + hero.data['AttributeStrengthGain'] * (level - 1),
            'attack_damage': hero.data['AttackDamageMin'] + hero.data['AttackDamageMax'] + hero.data['AttributeBaseAgility'] + hero.data['AttributeAgilityGain'] * (level - 1),
        }
    """

    # level_data = map(make_level_data, [1, 6, 12, 18, 25, 30])
    return template.hero.render(
        display_name=hero.display_name,
        strength=hero.data['AttributeBaseStrength'],
        strength_gain=float_eye(hero.data['AttributeStrengthGain']),
        agility=hero.data['AttributeBaseAgility'],
        agility_gain=float_eye(hero.data['AttributeAgilityGain']),
        intelligence=hero.data['AttributeBaseIntelligence'],
        intelligence_gain=float_eye(hero.data['AttributeIntelligenceGain']),
        # level_data=level_data,
    )


def main():
    os.makedirs('output/hero', exist_ok=True)
    for hero_id in hero_id_list():
        hero = get_hero(hero_id)
        html = render_hero(hero_id)
        name = hero.display_name.replace(' ', '_')
        with open('output/hero/' + name + '.html', 'w') as f:
            f.write(html)


if __name__ == "__main__":
    main()
