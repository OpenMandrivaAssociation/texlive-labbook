# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/labbook
# catalog-date 2012-04-26 13:32:32 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-labbook
Version:	20120426
Release:	1
Summary:	Typeset laboratory journals
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/labbook
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/labbook.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/labbook.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/labbook.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This class is designed to typeset laboratory journals that
contain chronologically ordered records about experiments. From
the sectioning commands, an experiment index is generated. The
class is based on the KOMA-Script class scrbook.cls. There can
be several index entries for one experiment.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/labbook/labbook.cls
%doc %{_texmfdistdir}/doc/latex/labbook/README
%doc %{_texmfdistdir}/doc/latex/labbook/boilerplates.tex
%doc %{_texmfdistdir}/doc/latex/labbook/examplde.tex
%doc %{_texmfdistdir}/doc/latex/labbook/examplen.tex
%doc %{_texmfdistdir}/doc/latex/labbook/labboode.pdf
%doc %{_texmfdistdir}/doc/latex/labbook/labboode.tex
%doc %{_texmfdistdir}/doc/latex/labbook/labbook.el
%doc %{_texmfdistdir}/doc/latex/labbook/labbook.pdf
#- source
%doc %{_texmfdistdir}/source/latex/labbook/labbook.dtx
%doc %{_texmfdistdir}/source/latex/labbook/labbook.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
