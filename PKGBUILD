# Script generated with Bloom
pkgdesc="ROS - Provides Python to ROS multiprocess API, useful for using ROS from different multiprocess environment while keeping both isolated."


pkgname='ros-kinetic-pyros'
pkgver='0.4.1_2'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('python2-mock>=1.0.1'
'ros-kinetic-catkin-pip>=0.2.0'
'ros-kinetic-catkin>=0.6.18'
'ros-kinetic-pyros-common>=0.4.2'
'ros-kinetic-pyros-interfaces-ros>=0.4.0'
)

depends=('python2-mock>=1.0.1'
'ros-kinetic-pyros-common>=0.4.2'
'ros-kinetic-pyros-interfaces-ros>=0.4.0'
)

conflicts=()
replaces=()

_dir=pyros
source=()
md5sums=()

prepare() {
    cp -R $startdir/pyros $srcdir/pyros
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

