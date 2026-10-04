# Certificate Generator

Generate personalized finalist and participation certificates from JPEG templates and lists of names. The two Python scripts use Pillow to center each name horizontally on its template and save one JPEG certificate per name.

## Requirements

- Python 3
- [Pillow](https://pillow.readthedocs.io/)
- Windows, if using the paths in the scripts as supplied

Install the Python dependency:

```powershell
py -m pip install Pillow
```

## Project layout

```text
Finalist_Cert_Generator/
  Finalist_cert.py             Finalist certificate script
  Finalist.jpeg                Certificate template
  Finalist_names.txt           One recipient name per line
  ARIAL.TTF                    Font used for names
Participation_Cert_Generator/
  Participation_cert.py        Participation certificate script
  participation.jpeg           Certificate template
  Participation_names.txt      One recipient name per line
  ARIAL.TTF                    Font used for names
Generated_Finalist_JPEGs/      Created when the finalist script runs
Generated_Participation_JPEGs/ Created when the participation script runs
```

## Generate certificates

1. Place the repository at `C:\Cert_Generator`, or update `template_path`, `font_path`, `names_file`, and `output_dir` near the top of **both** scripts to match its location. The supplied paths are absolute.
2. Edit the relevant `*_names.txt` file. Put one name on each line; blank lines are ignored.
3. From the repository folder, run either or both scripts:

   ```powershell
   py .\Finalist_Cert_Generator\Finalist_cert.py
   py .\Participation_Cert_Generator\Participation_cert.py
   ```

The scripts create their output folders if needed. Finalist certificates are saved in `Generated_Finalist_JPEGs`; participation certificates are saved in `Generated_Participation_JPEGs`. Each output file is named after its recipient, for example `Jane Doe.jpeg`.

## Customize the design

Edit the configuration values near the top of the appropriate script:

| Setting | Finalist | Participation |
| --- | --- | --- |
| Template | `Finalist.jpeg` | `participation.jpeg` |
| Name color | White | Black |
| Font size | 120 px | 120 px |
| Vertical position (`y_position`) | 550 px | 750 px |

The horizontal position is calculated from the template width and rendered text width. If you change the template or font, adjust `font_size`, `text_color`, and `y_position` to suit the new design.

**Note:** Output filenames come directly from the names list. Use names that are valid Windows filenames, and keep names unique within each list. Running a script again replaces existing JPEGs with the same names.
