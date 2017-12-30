# revision 24732
# category Package
# catalog-ctan /fonts/fge
# catalog-date 2011-11-18 06:50:27 +0100
# catalog-license lppl
# catalog-version 1.24
Name:		texlive-fge
Version:	1.25
Release:	1
Summary:	A font for Frege's Grundgesetze der Arithmetik
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/fge
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fge.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fge.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fge.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.24-2
+ Revision: 751833
- Rebuild to reduce used resources

* Fri Dec 09 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.24-1
+ Revision: 739750
- texlive-fge

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.22-1
+ Revision: 718429
- texlive-fge
- texlive-fge
- texlive-fge
- texlive-fge

