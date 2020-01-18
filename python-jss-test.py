#!/usr/bin/python

import jss


def main():
    """Main process."""
    jss_prefs = jss.JSSPrefs()
    j = jss.JSS(jss_prefs)
    print(j.Policy())


if __name__ == "__main__":
    main()
