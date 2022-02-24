import argparse
import yaml
import pdos
import funcpot


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config",
                help="Obtain smeared Projected density of states", nargs="+")
    args = parser.parse_args()
    
    if args.config:
        for i in args.config:
            with open(i,"r") as yamlfile:
                cfg = yaml.load(yamlfile, Loader=yaml.FullLoader)
            system = pdos.projected_dos(cfg)
            system.generate_pdos()

