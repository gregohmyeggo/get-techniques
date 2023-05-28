from attackcti import attack_client
import json, logging, random

class colors:
    GREEN = '\033[92m'
    DEBUG = '\033[93m'
    END = '\033[0m'

logging.getLogger('taxii2client').setLevel(logging.CRITICAL)

print(f'\n{colors.DEBUG}Fetching ATT&CK Data...{colors.END}\n')

lift = attack_client()
techniques = lift.get_techniques()

all_techniques = []
for t in techniques:
    all_techniques.append(json.loads(t.serialize()))

def get_random_technique():
    tactics = ['execution','persistence','privilege-escalation','defense-evasion','credential-access','discovery','lateral-movement']
    randotech = all_techniques[random.randint(0, len(all_techniques))]

    if 'Windows' in randotech['x_mitre_platforms']:
    
        phases = []
        for kcp in randotech['kill_chain_phases']:
            phases.append(kcp['phase_name'])
        
        for tactic in tactics:
            if tactic in phases:
                print(f'Tactic: {colors.GREEN}{tactic.upper()}{colors.END}')
                return randotech

def main():
    technique = []

    while len(technique) == 0:
        randotech = get_random_technique()
        if randotech:
            technique.append(randotech['name'])
            print(f'Technique: {colors.CYAN}{technique[0]}{colors.END}\n')
            print(json.dumps(randotech, indent=4))

main()
