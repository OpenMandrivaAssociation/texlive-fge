# revision 15878
# category Package
# catalog-ctan /fonts/fge
# catalog-date 2009-03-12 01:27:31 +0100
# catalog-license lppl
# catalog-version 1.22
Name:		texlive-fge
Version:	1.22
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The fonts are provided as MetaFont source and Adobe Type 1
(pfb) files. A small LaTeX package (fge) is included.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
