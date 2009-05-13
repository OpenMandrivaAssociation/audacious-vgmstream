%define name audacious-vgmstream
%define oname vgmstream
%define version 0
%define svn r601
%define release %mkrel 0.%svn.2

Summary: Audacious plugin for playback of various streamed video game formats
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{oname}-%{svn}.tar.gz
Patch: vgmstream-r601-audacious-includes.patch
License: MIT
Group: Sound
Url: https://sourceforge.net/projects/vgmstream/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libaudacious-devel
BuildRequires: libmpg123-devel
BuildRequires: libvorbis-devel
BuildRequires: gtk+2-devel
Requires: audacious
Provides: audacious-cube
Obsoletes: audacious-cube

%description
This is vgmstream, a library for playing streamed audio from video games.

%prep
%setup -q -n %oname-%svn
%patch -p1
./bootstrap

%build
export CPPFLAGS=-D_FILE_OFFSET_BITS=64
%configure2_5x
%make -f Makefile.unix

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std  -f Makefile.unix
rm -f %buildroot%_libdir/audacious/Input/libvgmstream.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc *.txt
%_libdir/audacious/Input/libvgmstream.so
