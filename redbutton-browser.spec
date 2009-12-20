Name:           redbutton-browser
Version:        20091202
Release:        %mkrel 1
Group:          Development/Other 
License:        GPLv2+
Summary:        Redbutton browser for MHEG5 content
Source:         redbutton-browser-%{version}.tar.gz
Patch0:	        redbutton-browser-20091202-lib64swscale.patch
URL:            http://redbutton.sourceforge.net/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:  ffmpeg-devel
BuildRequires:  libexpat-devel
BuildRequires:  libxrender-devel
BuildRequires:  libxft-devel
BuildRequires:  libpng-devel
BuildRequires:  xsltproc

%description
This package provides a browser for MHEG5, which is used to make
user interface on TVs.
It is part of the redbutton tools suite.

%prep
%setup -q
%patch0

%build
make

%install
%__rm -rf %{buildroot}
mkdir -p %buildroot%_bindir
#make install DESTDIR=%buildroot # happens "/bin" to DESTDIR
install -m 755 rb-browser %buildroot%_bindir
install -m 755 rb-keymap %buildroot%_bindir

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%_bindir/rb-browser
%_bindir/rb-keymap



