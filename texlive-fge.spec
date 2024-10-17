Name:		texlive-fge
Version:	71737
Release:	1
Summary:	A font for Frege's Grundgesetze der Arithmetik
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/fge
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fge.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fge.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fge.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The fonts are provided as Metafont source and Adobe Type 1
(pfb) files. A small LaTeX package (fge) is included.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/map/dvips/fge/fge.map
%{_texmfdistdir}/fonts/source/public/fge/fgebase.mf
%{_texmfdistdir}/fonts/source/public/fge/fgeit.mf
%{_texmfdistdir}/fonts/source/public/fge/fgeit10.mf
%{_texmfdistdir}/fonts/source/public/fge/fgerm.mf
%{_texmfdistdir}/fonts/source/public/fge/fgerm10.mf
%{_texmfdistdir}/fonts/tfm/public/fge/fgeit10.tfm
%{_texmfdistdir}/fonts/tfm/public/fge/fgerm10.tfm
%{_texmfdistdir}/fonts/type1/public/fge/fgeit10.pfb
%{_texmfdistdir}/fonts/type1/public/fge/fgerm10.pfb
%{_texmfdistdir}/tex/latex/fge/Ufgeit.fd
%{_texmfdistdir}/tex/latex/fge/Ufgerm.fd
%{_texmfdistdir}/tex/latex/fge/fge.cfg
%{_texmfdistdir}/tex/latex/fge/fge.sty
%doc %{_texmfdistdir}/doc/fonts/fge/README
%doc %{_texmfdistdir}/doc/fonts/fge/fge-doc.pdf
#- source
%doc %{_texmfdistdir}/source/fonts/fge/fge.dtx
%doc %{_texmfdistdir}/source/fonts/fge/fge.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
