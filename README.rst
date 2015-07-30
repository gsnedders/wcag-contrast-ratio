wcag-contrast-ratio
===================

A library for computing contrast ratios, as required by `WCAG 2.0`.

Usage
-----

Simple usage follows this pattern:

.. code-block:: python

  >> import wcag_contrast_ratio as contrast
  >> black = (0.0, 0.0, 0.0)
  >> white = (1.0, 1.0, 1.0)
  >> contrast.rgb(black, white)
  21.0

Two useful helper functions are provided, to check if contrast meets
the required level:

.. code-block:: python

  >> import wcag_contrast_ratio as contrast
  >> contrast.passes_AA(21.0)
  True
  >> contrast.passes_AAA(21.0)
  True

.. _WCAG 2.0: http://www.w3.org/TR/WCAG20/
