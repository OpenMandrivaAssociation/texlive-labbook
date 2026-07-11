%global tl_name labbook
%global tl_revision 15878

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Typeset laboratory journals
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/labbook
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/labbook.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/labbook.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/labbook.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This class is designed to typeset laboratory journals that contain
chronologically ordered records about experiments. From the sectioning
commands, an experiment index is generated. The class is based on the
KOMA-Script class scrbook.cls. There can be several index entries for
one experiment.

