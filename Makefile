SHELL := /bin/sh
PYTHON ?= $(RESEARCH_PYTHON)
PDFLATEX ?= pdflatex
export SOURCE_DATE_EPOCH := 1794614400
export FORCE_SOURCE_DATE := 1
export MPLCONFIGDIR := $(CURDIR)/tmp/matplotlib
export OPENBLAS_NUM_THREADS := 1
export OMP_NUM_THREADS := 1
export VECLIB_MAXIMUM_THREADS := 1

.PHONY: paper check verify figure numerics require-python
require-python:
	@test -n "$(PYTHON)" || { echo 'Set PYTHON to an absolute virtual-environment interpreter path.'; exit 1; }
	@case "$(PYTHON)" in /*) ;; *) echo 'PYTHON must be an absolute path.'; exit 1;; esac
	@"$(PYTHON)" -c 'import sys; assert sys.prefix != sys.base_prefix'

# Four passes from a clean extraction; no inherited auxiliaries are required.
paper:
	cd paper && $(PDFLATEX) -interaction=nonstopmode -halt-on-error main.tex
	cd paper && $(PDFLATEX) -interaction=nonstopmode -halt-on-error main.tex
	cd paper && $(PDFLATEX) -interaction=nonstopmode -halt-on-error main.tex
	cd paper && $(PDFLATEX) -interaction=nonstopmode -halt-on-error main.tex
	@! grep -E 'Warning:|Overfull|Underfull|undefined references|undefined citations' paper/main.log

check: require-python
	"$(PYTHON)" scripts/check_paper.py

verify: require-python
	"$(PYTHON)" c1_certificate.py
	"$(PYTHON)" scripts/verify_numerics.py
	"$(PYTHON)" scripts/cf_checks.py

figure: require-python
	"$(PYTHON)" fig_asymptotics.py --plot-only

numerics: require-python
	"$(PYTHON)" checks.py
	"$(PYTHON)" large_x.py 4
	"$(PYTHON)" secular_c1.py
	"$(PYTHON)" fig_asymptotics.py
