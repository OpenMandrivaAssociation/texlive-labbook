Name:		texlive-labbook
Version:	15878
Release:	2
Summary:	Typeset laboratory journals
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/labbook
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/labbook.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/labbook.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/labbook.source.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/labbook
%doc %{_texmfdistdir}/doc/latex/labbook
#- source
%doc %{_texmfdistdir}/source/latex/labbook

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
