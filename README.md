# Python_FPL_export
Example of how to export longitude and latitude to a Garmin FPL file format

This exporter example was created as part of a proposed solution for the Civil Air Patrol (CAP) to export a Garmin FPL file from a set of longitude and latitude points created by another process.  These files were able to be imported into the Garmin G1000 avionics system.

In this case, they were lines going back and forth over an area, but you can create whatever points you want in the order you want to fly them in.

I couldn't find an exporter library, so I used certain functions in the code released by the British Antarctic Survey.  Specifically:  https://github.com/antarctica/bas-air-unit-network-dataset

I included an FPL file in the sample_output directory so you can see what it looks like.

# Installation

As always, it is recommended to install in a virtual environment to isolate it from the rest of your system.



```
git clone https://github.com/jimburtoft/Python_FPL_export.git
cd Python_FPL_export
python -m venv fpl-env
fpl-env\Scripts\activate
(fpl-env)python -m pip install -r requirements.txt
(fpl-env)python -m export_fpl.py
```

If you don't change the output directory, you will also need to create C:\OutputDir\FPLdir