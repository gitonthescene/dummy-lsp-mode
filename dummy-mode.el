;;; dummy-mode.el --- major-mode and a few utilities for working with ngn/k. -*- lexical-binding: t; -*-

;;;###autoload
(define-derived-mode dummy-mode text-mode "DummyLSP"
  "Dummy mode for testing basic LSP features.

\\<dummy-mode-map>"
  nil "DummyLSP")


(provide 'dummy-mode)
;;; dummy-mode.el ends here
