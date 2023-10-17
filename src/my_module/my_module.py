from my_module.tools import really_important_function


# this is the function we call from the entry_points/console_scripts
def main():
    really_important_function()


if __name__ == "__main__":  # pragma: no cover
    main()
